import logging as log

log.basicConfig(
    filename=log.FileHandler('datascience.log')
    ,level=log.INFO)

def info(msg):
    log.info(msg)
    
def debug(msg):
    log.debug(msg)

def warning(msg):
    log.warning(msg)

def error(msg):
    log.error(msg)
    
def critical(msg):
    log.critical(msg)