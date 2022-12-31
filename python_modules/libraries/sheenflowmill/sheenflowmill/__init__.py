from sheenflow._core.utils import check_dagster_package_version

from .asset_factory import define_dagstermill_asset
from .context import DagstermillExecutionContext
from .errors import DagstermillError
from .factory import define_dagstermill_op
from .io_managers import local_output_notebook_io_manager
from .manager import MANAGER_FOR_NOTEBOOK_INSTANCE as _MANAGER_FOR_NOTEBOOK_INSTANCE
from .version import __version__

check_dagster_package_version("sheenflowmill", __version__)

get_context = _MANAGER_FOR_NOTEBOOK_INSTANCE.get_context

yield_result = _MANAGER_FOR_NOTEBOOK_INSTANCE.yield_result

yield_event = _MANAGER_FOR_NOTEBOOK_INSTANCE.yield_event

_reconstitute_pipeline_context = _MANAGER_FOR_NOTEBOOK_INSTANCE.reconstitute_pipeline_context

_teardown = _MANAGER_FOR_NOTEBOOK_INSTANCE.teardown_resources

_load_input_parameter = _MANAGER_FOR_NOTEBOOK_INSTANCE.load_input_parameter
