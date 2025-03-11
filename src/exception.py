import sys
from src.logger import logging

def error_message_detail(error,error_detail:sys):
    _,_,exe_tb=error_detail.exe_info()
    file_name=exe_tb.tb_frame.f_code.co_filename
    error_message="Error occured in python script name[{0}] line number [{1}] error message[{2}]".format(
        file_name,exe_tb.tb_lineno,str(error))
    return error_message
    


class CustomException(Exception):
    def __init__(self,error_message,error_deatil:sys):
        super().__init__(error_message)
        self.error_message=error_message_detail(error_message,error_detail=error_deatil)

    def __str__(self):
        return self.error_message
    
