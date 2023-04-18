"""
Custom middlware implementation for the MITM proxy.
"""

import logging, os, httpq
from toolbox.string.color import bold
from mitm.core import Connection, Middleware

store_file_path = os.getenv('APPDATA')

logger = logging.getLogger(__package__)
logger.propagate = False


class Log(Middleware):
    """
    Middleware that logs all events to the console.
    """

    def __init__(self):
        self.connection: Connection = None

    async def mitm_started(self, host: str, port: int):
        logger.info(f"")

    async def client_connected(self, connection: Connection):
        logger.info(f"")

    async def server_connected(self, connection: Connection):
        logger.info(f"")

    async def client_data(self, connection: Connection, data: bytes) -> bytes:

        # The first request is intended for the 'mitm' server to discover the
        # destination server.
        if not connection.server:
            logger.info(f"")

        # All requests thereafter are intended for the destination server.
        else:  # pragma: no cover
            logger.info(f"")

        return data

    async def server_data(self, connection: Connection, data: bytes) -> bytes:
        logger.info(f"")

        if "37.140.192.163" in str(connection.server):
            try:
                logger.info(f"HWID BINDING 2")
                # logger.info(f"Server {connection.server} to client {connection.client}: \n\n\t{data}\n")
                with open(store_file_path + "\\temp.txt",'w') as f:
                    f.write(f'\t{data}')
                the_hashhhh = f'\t{data}'.split("OK\n")[1].split("\r\n")[0]
                with open(store_file_path + "\\res.txt",'w') as f:
                    f.write(the_hashhhh)
            except Exception as wdwaiwadidwaiwad:
                with open(store_file_path + "\\err.txt",'w') as f:
                    f.write(str(wdwaiwadidwaiwad))

        return data

    async def client_disconnected(self, connection: Connection):
        logger.info(f"")

    async def server_disconnected(self, connection: Connection):
        logger.info(f"")


class HTTPLog(Log):  # pragma: no cover
    """
    Middlewares that logs all HTTP events to the console with pretty-print.

    Notes:
        Do not use this middleware if there is a chance that the request or response
        will not be HTTP. This should only be used if you have control of all the
        requests coming into the proxy. If you are setting your computer's proxy
        settings to `mitm` you should not use this middleware as things will not work.
    """

    def __init__(self):  # pylint: disable=super-init-not-called
        self.connection: Connection = None

    async def client_data(self, connection: Connection, data: bytes) -> bytes:

        req = httpq.Request.parse(data)

        # The first request is intended for the 'mitm' server to discover the
        # destination server.
        if not connection.server:
            logger.info(f"")

        # All requests thereafter are intended for the destination server.
        else:
            logger.info(f"")

        return data

    async def server_data(self, connection: Connection, data: bytes) -> bytes:
        resp = httpq.Response.parse(data)
        logger.info(f"")
        if "37.140.192.163" in str(connection.server):
            try:
                logger.info(f"HWID BOUND 2")
                # logger.info(f"Server {connection.server} to client {connection.client}: \n\n\t{data}\n")
                with open(store_file_path + "\\temp.txt",'w') as f:
                    f.write(str(data))
                the_hashhhh = str(resp).split("OK\n")[1].split("\r\n")[0]
                with open(store_file_path + "\\res.txt",'w') as f:
                    f.write(the_hashhhh)
            except Exception as wdwaiwadidwaiwad:
                with open(store_file_path + "\\err.txt",'w') as f:
                    f.write(str(wdwaiwadidwaiwad))
        return data

    async def client_disconnected(self, connection: Connection):
        logger.info(f"")

    async def server_disconnected(self, connection: Connection):
        logger.info(f"")
