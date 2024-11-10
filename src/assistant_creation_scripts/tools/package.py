packaged_tools = []

packaged_tools_funcs = []

from .query_funcs import __getProductInfoByName, __getProductStockById

packaged_tools_funcs.append(__getProductInfoByName)

packaged_tools_funcs.append(__getProductStockById)
