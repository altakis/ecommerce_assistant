from .get_product_info_by_category import (
    _getProductInfoByCategory,
    _getProductInfoByCategory_tool_definition,
)
from .get_product_info_by_name import (
    _getProductInfoByName,
    _getProductInfoByName_tool_definition,
)
from .get_product_stock_by_id import (
    _getProductStockById,
    _getProductStockById_tool_definition,
)

def get_tools():
    tools = [
        _getProductInfoByName_tool_definition,
        _getProductStockById_tool_definition,
        _getProductInfoByCategory_tool_definition,
    ]
    
    return tools