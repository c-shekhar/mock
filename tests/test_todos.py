# # Third-party imports...
# from nose.tools import assert_is_not_none

# # Local imports...
# from src.services import get_todos


# def test_request_response():
#     # Call the service, which will send a request to the server.
#     response = get_todos()

#     # If the request is sent successfully, then I expect a response to be returned.
#     assert_is_not_none(response)


# # Standard library imports...
# from unittest.mock import Mock, patch

# # Third-party imports...
# from nose.tools import assert_is_not_none

# # Local imports...
# from src.services import get_todos


# @patch('src.services.requests.get')
# def test_getting_todos(mock_get):
#     # Configure the mock to return a response with an OK status code.
#     mock_get.return_value.ok = True

#     # Call the service, which will send a request to the server.
#     response = get_todos()

#     # If the request is sent successfully, then I expect a response to be returned.
#     assert_is_not_none(response)


# Standard library imports...
from unittest.mock import Mock, patch

# Third-party imports...
from nose.tools import assert_is_not_none

# Local imports...
from src.services import TodoClient
todo_client = TodoClient()

@patch('src.services.requests.get')
def test_getting_todos(mock_get):
    # Configure the mock to return a response with an OK status code.
    mock_get.return_value.ok = True

    # Call the service, which will send a request to the server.
    response = todo_client.get_todos()

    # If the request is sent successfully, then I expect a response to be returned.
    assert_is_not_none(response)

