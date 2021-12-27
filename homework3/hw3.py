import asyncio
import websockets
import json

tradefile=open("file.txt","w")

async def upbit_ws_client():
    uri="wss://api.upbit.como/websocket/v1"

    async with websockets.connect(uri) as websocket:
        subscribe_fmt=[
            {"ticket":"UNIQUE_TICKET"},
            {
                "type":"trade",
                "codes":["KRW-BTC"],
            },
            {
                "type":"orderbook"
                "codes":["KRW-BTC"]
            }
        ]

        subscribe_data=json.dumps(subscribe_fmt)
        await websocket.send(subscribe_data)

        while True:
            data=await websocket.recv()
            data=json.loads(data)

            if(data['type']=='orderbook'):
                List=[]
                newDate=data["orderbook_units"][0]
                for i in newData:
                    line=str(i+": "+str(newData[i]))
                    List.append(line)
                print(", ".join(List))
                tradefile.write(", ".join(List)+"\n")
            elif(data['type']=='trade'):
                List=[]
                newData=data
                info=['trade_price', 'trade_volume','ask_bid']
                for i in info:
                    line=str(i+": "+str(newData[i]))
                    List.append(line)
                print(", ".join(List))
async def main():
    await upbit_ws_client()

if __name__=="__main__":
    try:
        asyncio.run*main())
    except KeyboardInterrupt:
        print("Ctrl+C Stop!")
    tradefile.close