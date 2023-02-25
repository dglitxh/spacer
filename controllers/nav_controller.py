import os
import json
from models import models, schema
from common.logger import logger
from datetime import datetime, timedelta
from fastapi import Depends, FastAPI, HTTPException, APIRouter, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from common.db import rdb
from dotenv import load_dotenv