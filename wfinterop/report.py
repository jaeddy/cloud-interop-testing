def get_checker_queues():
    return [(queue_id, queue['target_queue'])
            for queue_id, queue in queue_config().items()
            if queue['target_queue']]

def get_complete(testbed_log, queue_id):
    complete_subs = [(wes_id, sub_id)
                     for wes_id, subs in testbed_log[queue_id].items()
                     for sub_id, data in subs.items()
                     if data['status'] == 'COMPLETE']
    return dict(complete_subs)

def get_verified_details(queue_id):
    complete_subs = get_complete(get_json(testbed_log), queue_id)
    details = []
    for wes_id, sub_id in complete_subs.items():
        wes_data = wes_config()[wes_id]
        sub_data = get_json(submission_queue)[queue_id][sub_id]
        details.append({'wes_url': '{}//{}'.format(wes_data['proto'], wes_data['host']),
                        'test_url': sub_data['data'],
                        'wes_run_id': sub_data['run_log']['run_id'],
                        'test_date': sub_data['run_log']['start_time']})
    return details

def testbed_result(checker_queue, target_queue):
    target_data = queue_config()[target_queue]
    try:
        verified_details = get_verified_details(checker_queue)
    except KeyError:
        verified_details = False
    wes_results = {'workflow_id': target_data['workflow_id'],
                   'version_id': target_data['version_id'],
                    'wes_verified': verified_details}
    return wes_results

def testbed_report():
    foo = []
    for checker_target in get_checker_queues():
        foo.append(testbed_result(checker_target[0], checker_target[1]))
    return foo
