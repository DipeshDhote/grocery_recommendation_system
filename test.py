import sys
from src.grocery_recommendation_system.logger import logging
from src.grocery_recommendation_system.exception import CustomException



if __name__=="__main__":
    logging.info("The logging file is created")

    try:
        a =1/0


    except Exception as e:
        logging.info("The custom exception is created")
        raise CustomException(e,sys)