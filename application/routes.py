from flask import request, render_template

from application import app
from application.api_response import ApiResponse
from application.errors import ApiException
from application.models import BankBranches
from application.validations import Validator


@app.route('/', methods=['POST', 'GET'])
def search():
    # if request.method == 'POST':
    #     options = request.form.getlist('options')
    #     if not options:
    #         return render_template('index.html')
    #     else:
    #         if options[0] == 'Search by IFSC':
    #             return render_template('index.html')
    #         if options[0] == 'Search by name':
    #             return {}
    return render_template('index.html')


@app.route("/get_by_ifsc/<ifcs_code>", methods=['GET'])
def get_by_ifsc(ifcs_code):
    result = BankBranches.query.get(ifcs_code)
    if not result:
        return ApiResponse.get_error_response(message='Invalid IFSC', status_code=404)
    return ApiResponse.get_success_response(result.serialize)


@app.route("/get_by_name", methods=['GET'])
def get_by_name():
    try:
        query_params = request.args.to_dict()
        Validator.validate_search_input(query_params)
        sort_by_key = query_params.pop('sort_by') if 'sort_by' in query_params else None
        base_query = BankBranches.query.filter_by(**query_params)
        if sort_by_key:
            result = base_query.order_by(sort_by_key).all()
        else:
            result = base_query.all()
        if not result:
            return ApiResponse.get_error_response(message='Bank Details not found', status_code=404)
        return ApiResponse.get_success_response(BankBranches.serialize_list(result))
    except ApiException as e:
        return ApiResponse.get_error_response(e.message, e.status_code)
    except Exception as e:
        import traceback
        print(traceback.format_exc())
        return ApiResponse.get_error_response()
