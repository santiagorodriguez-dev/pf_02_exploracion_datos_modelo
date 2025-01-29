import pandas as pd
import sys
sys.path.append("../")
import dotenv # type: ignore
dotenv.load_dotenv()

# import warnings
# warnings.filterwarnings("ignore")

from src import support_visualizacion as spv

def visual():
   spv.visualiazar_datos_alumnos()

def main():
   visual()
   
if __name__ == "__main__":
   main()
