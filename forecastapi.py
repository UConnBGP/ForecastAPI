from flask import Flask, jsonify
from flasgger import Swagger, swag_from
from random import random

app = Flask(__name__, static_url_path='/extrapolation_results')
swagger = Swagger(app)

asn_stats = {
  'simpleTimeHeuristic': {
      'neitherBlockedNorHijacked': int(random() * 100),
      'hijackedAndBlocked': int(random() * 100),
      'notHijackedButBlocked': int(random() * 100),
      'hijackedButNotBlocked': int(random() * 100)
  },
  'rov': {
      'neitherBlockedNorHijacked': int(random() * 100),
      'hijackedAndBlocked': int(random() * 100),
      'notHijackedButBlocked': int(random() * 100),
      'hijackedButNotBlocked': int(random() * 100)
  }
}

@app.route('/asn_hijack_stats/<asn>/<policy>/')
@swag_from('flasgger_docs/asn_hijack_stats.yml')
def asn_hijack_stats(asn, policy):
    policies = ['simpleTimeHeuristic', 'rov']

    result = {}
    if policy == 'all':
        for ply in policies:
            result[asn] = asn_stats
    else:
        result[asn] = asn_stats[policy]

    return jsonify(result)

@app.route('/extrapolation/<asn>/')
@swag_from('flasgger_docs/extrapolation.yml')
def extrapolation(asn):
    return app.send_static_file('extrapolation_results.csv')
