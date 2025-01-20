from sanic import Sanic
from sanic.response import json
from controller import *
app = Sanic("ErrorHandlingExample")

@app.post("/openai")
async def openai(request):
    try:
        data = request.json
        response = AzureOpenAIController(data)
        return json(response)
    except Exception as e:
        print(f"Error in Transcribe Summary: {str(e)}")
        return json({
                "Error":str(e),
                "statusCode":500
            })
    
@app.post("/google")
async def google(request):
    try:
        data = request.json
        response = AzureOpenAIController(data)
        return json(response)
    except Exception as e:
        print(f"Error in Transcribe Summary: {str(e)}")
        return json({
                "Error":str(e),
                "statusCode":500
            })
    
    

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000,debug=True)
