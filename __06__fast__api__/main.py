from fastapi import FastAPI
from indb import load_products

# import asyncio
import uvicorn

app = FastAPI()

products = load_products()

@app.get('/products')
def get_products():
    return {'products' : products}

if __name__ == '__main__':
    uvicorn.run(app= app, host= '127.0.0.1', port= 3001)

# async def main():
#     uvicorn.run(app= app, host= '127.0.0.1', port= 3001)
    
# if __name__ == '__main__':
#     asyncio.run(main())