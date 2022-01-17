from socket import MsgFlag


class LogMixin:
    @staticmethod
    def write(msg):
        with open('log.log', 'a+') as f:
            f.write(msg)
            f.write('\n')
    
    def logInfo(self, msg):
        self.write(f'INFO: {msg}')
    
    def logError(self, msg):
        self.write(f'ERROR: {msg}')
            
# Como não usa self, ele é estático