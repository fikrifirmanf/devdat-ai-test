from flask import jsonify

def custom_response(data=None, status=200, message=None, error=None):
    """
    Custom jsonify function for Flask responses.

    Args:
        data: The data to be returned in the JSON response.
        status: The HTTP status code.
        message: A success message.
        error: An error message (if applicable).

    Returns:
        A Flask jsonify response object.
    """
    response = {}
    if data is not None:
        response['data'] = data
    if message is not None:
        response['message'] = message
    if error is not None:
        response['error'] = error
    return jsonify(response), status