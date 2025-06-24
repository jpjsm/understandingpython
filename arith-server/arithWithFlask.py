import flask
from flask import Flask, request, jsonify
import arith

main = Flask("Arithmetic")

@main.route("/isprime", methods=['GET'])
def test_isprime():
    args = request.args.to_dict()
    results = []
    for argname in args:
        n = args[argname]
        try:
            result = str(arith.isprime(n))
        except:
            result = "invalid argument for isprime()"
        finally:
            results.append("<p>{0} = {1}, is prime? <b>{2}</b></p>".format(argname, n, result))

    return "\n".join(results)

@main.route("/isodd", methods=['GET'])
def test_isodd():
    args = request.args.to_dict()
    results = []
    for argname in args:
        n = args[argname]
        try:
            result = str(arith.isodd(n))
        except:
            result = "invalid argument for isodd()"
        finally:
            results.append("<p>{0} = {1}, is odd? <b>{2}</b></p>".format(argname, n, result))

    return "\n".join(results)

@main.route("/iseven", methods=['GET'])
def test_iseven():
    args = request.args.to_dict()
    results = []
    for argname in args:
        n = args[argname]
        try:
            result = str(arith.iseven(n))
        except:
            result = "invalid argument for iseven()"
        finally:
            results.append("<p>{0} = {1}, is even? <b>{2}</b></p>".format(argname, n, result))

    return "\n".join(results)
@main.route("/", methods=['GET'])
def home():
    Rq = request.environ
    return jsonify(Rq),200

if __name__ == "__main__":
    main.run(host='0.0.0.0')