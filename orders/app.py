from fastapi import FastAPI

app = FastAPI(debug=True)

from orders import api