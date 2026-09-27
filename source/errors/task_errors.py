class TaskError(Exception):
    """작업 실행과 관련된 모든 에러"""

class FailedRunError(TaskError):
    """작업 실행에 실패함"""
    pass

