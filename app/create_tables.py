from db.create_tables import init_models
import asyncio

if __name__ == '__main__':
    asyncio.run(init_models())
