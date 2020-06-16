from functools import reduce

def reduce_map_filter(args_):
    
    if type(args_[2]) is tuple:
        
        args_ = (args_[0],args_[1],reduce_map_filter(args_[2]))
        
    if args_[0] == "map":
        
        return list(map(args_[1], args_[2]))
    
    elif args_[0] == "reduce":
        return reduce(args_[1], args_[2])
    elif args_[0] == "filter":
        return list(filter(args_[1], args_[2]))