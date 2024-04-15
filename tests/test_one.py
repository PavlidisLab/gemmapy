import gemmapy

def test_one():
    api = gemmapy.GemmaPy()
    res = api.get_platforms_by_ids(['GPL96'])
    print(res)
