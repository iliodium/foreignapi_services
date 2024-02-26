import enum


class CountWorkersService(enum.IntEnum):
    BookkeepingService = 10


class BookkeepingServiceResponce(str, enum.Enum):
    pay_tax = "ПЛАТИ НАЛОГИ"


class StatusServer(str, enum.Enum):
    start = "running the gRPC server {}"
    success = "the gRPC server {} is successful running"
    error = "the gRPC server {} has crashed"
