import Module.collect

if __name__ == '__main__':
    url = 'https://api.datamuse.com/words'
   # params, headers = {'rel_rhy':'forgetful', 'sl':'jirraf'}, {}
    params, headers = {'ml':'breakfast'}, {}

    res = httpFetcher(url, 'get', params=params, headers = headers)
    res_format = formatResponse(res, "json")
   # print(res_format)
    print(getFilename(params))
    #getFilename(params)
    collectData(getFilename(params), 'files', res_format)