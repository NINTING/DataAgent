"""pytest配置文件"""

import pytest


def pytest_addoption(parser):
    """添加自定义命令行选项"""
    parser.addoption(
        "--runslow", action="store_true", default=False, help="运行慢速测试"
    )


def pytest_configure(config):
    """pytest配置"""
    config.addinivalue_line("markers", "slow: 标记慢速测试")
    config.addinivalue_line("markers", "integration: 标记集成测试")
    config.addinivalue_line("markers", "unit: 标记单元测试")
    config.addinivalue_line("markers", "api: 标记需要API调用的测试")


def pytest_collection_modifyitems(config, items):
    """根据命令行选项修改测试收集"""
    if not config.getoption("--runslow"):
        skip_slow = pytest.mark.skip(reason="需要 --runslow 选项运行慢速测试")
        for item in items:
            if "slow" in item.keywords:
                item.add_marker(skip_slow)
