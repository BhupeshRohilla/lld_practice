from abc import ABC, abstractmethod
from datetime import datetime

class ILogger(ABC):
    def __init__(self) -> None:
        self.proccess: dict[str, Process] = {}
    
    @abstractmethod
    def start(self, process_id: str) -> None: pass

    @abstractmethod
    def end(self, process_id: str) -> None: pass

    @abstractmethod
    def poll(self) -> None: pass

class Process:
    def __init__(self, id: str, start_time: datetime) -> None:
        self.__id = id
        self.__start_time = start_time
        self.__end_time = -1

    @property
    def id(self) -> str:
        return self.__id

    @property
    def start_time(self) -> datetime:
        return self.__start_time
    
    @property
    def end_time(self):
        return self.__end_time
    
    @end_time.setter
    def end_time(self, end_time) -> None:
        self.__end_time = end_time

class Logger(ILogger):
    def __init__(self) -> None:
        super().__init__()        
    
    def start(self, process_id: str) -> None:
        self.proccess[process_id] = Process(process_id, datetime.now())
    
    def end(self, process_id: str) -> None:
        self.proccess[process_id].end_time = datetime.now()

    def poll(self) -> None:
        if not self.proccess:
            print('Queue is empty!')
            return
        process_id = next(iter(self.proccess))
        process = self.proccess[process_id]
        if process.end_time != -1:
            print(f'{process_id} started at {process.start_time} and ended at {process.end_time}.')
            del(self.proccess[process_id])
        else:
            print(f'No completed task in queue: {process_id}')

if __name__ == '__main__':
    logger = Logger()
    logger.start('1')
    logger.poll()
    logger.start('3')
    logger.poll()
    logger.end('1')
    logger.poll()
    logger.start('2')
    logger.poll()
    logger.end('2')
    logger.poll()
    logger.end('3')
    logger.poll()
    logger.poll()
    logger.poll()
