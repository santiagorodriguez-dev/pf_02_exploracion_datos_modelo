import pandas as pd
import sys
sys.path.append("../")
import dotenv # type: ignore
dotenv.load_dotenv()

import warnings
warnings.filterwarnings("ignore")

from src import support_tsf as tsf

def modelo_predictivo_tsf():
   
   tsf.crear_modelo()

def main():
   modelo_predictivo_tsf()
   
if __name__ == "__main__":
   main()
