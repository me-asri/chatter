import argparse

import uvicorn

parser = argparse.ArgumentParser()
parser.add_argument('-b', '--bind', default='127.0.0.1',
                    help='Bind address')
parser.add_argument('-p', '--port', type=int, default=8000,
                    help='Port')
parser.add_argument('-r', '--reload', action='store_true',
                    help='Enable live reload')

args = parser.parse_args()

uvicorn.run(
    "chatter.main:app",
    host=args.bind,
    port=args.port,
    reload=args.reload
)
