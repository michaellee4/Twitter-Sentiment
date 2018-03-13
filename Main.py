import TwitterParse


coins = ['#btc','#bitcoin','#eth','#ethereum','#cryptocurrency','#crypto', '#blockchain']
trump = ['trump']
params = trump

x = TwitterParse

# params must be a list of desired filters and an integer number of seconds
x.tweetStream(params, 20)
