from fastapi import FastAPI
from fastapi.responses import JSONResponse
import json

from .logic import sort_numbers_by_bitcount
from .models import SortRequest, SortResponse

app = FastAPI(title="Sort Integers by BitCount")


@app.post("/sort", response_model=SortResponse)
def sort_endpoint(req: SortRequest):
    """Sort the provided list of integers by the number of 1 bits in their binary representation.

    Ties are broken by ascending integer value.
    """
    arr = req.numbers
    sorted_arr = sort_numbers_by_bitcount(arr)
    return SortResponse(sorted_numbers=sorted_arr)


@app.websocket("/ws")
async def websocket_sort(websocket):
    """WebSocket endpoint for sorting numbers on demand.

    Expects a JSON string with the structure: {"numbers": [int, int, ...]}
    Responds with {"sorted_numbers": [int, int, ...]} or {"error": "..."}.
    """
    await websocket.accept()
    try:
        text = await websocket.receive_text()
        data = json.loads(text)
        numbers = data.get("numbers")
        if not isinstance(numbers, list) or not all(isinstance(n, int) for n in numbers):
            await websocket.send_json({"error": "Invalid input. 'numbers' must be a list of integers."})
            await websocket.close()
            return
        sorted_arr = sort_numbers_by_bitcount(numbers)
        await websocket.send_json({"sorted_numbers": sorted_arr})
    except json.JSONDecodeError:
        await websocket.send_json({"error": "Invalid JSON."})
        await websocket.close()
    except Exception as e:
        await websocket.send_json({"error": str(e)})
        await websocket.close()
