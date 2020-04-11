import os
import logging

def log_init():
    """
    initialize logging 
    save the logging object in `config.Parameters.Logging_Object`
    
    after this operation,
    we could save logs with sample orders such as `logging.debug('test debug')` `logging.info('test info')` 
    logging level : debug < info < warning <error < critical
    """
    
    log_file_path = 'test_log.log'
    
    if os.path.exists(log_file_path):
        # open log file as  mode of append
        open_type = 'a'
    else:
        # open log file as  mode of write
        open_type = 'w'
        
    logging.basicConfig(
    
        # 日志级别,logging.DEBUG,logging.ERROR
        level = logging.INFO,  

        # 日志格式: 时间、      代码所在文件名、代码行号、         日志级别、       日志信息
        format = '%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
    
        # 打印日志的时间
        datefmt = '%a, %Y-%m-%d %H:%M:%S',
    
        # 日志文件存放的目录（目录必须存在）及日志文件名
        filename = log_file_path, 
    
        # 打开日志文件的方式
        filemode = open_type
    )    
    
    
        
if __name__ =='__main__':
    
    ## init logging
    log_init()    
    
    ## print log
    
    logging.debug('debug')  # this message won't be wrote to the log file, for the priority of DEBUG is lower than INFO
    logging.info('info')
    logging.warning('warning')
    logging.error('error')
    logging.critical('critical')    
    
        
        
        
        
        
       