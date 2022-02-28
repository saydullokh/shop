function getParamSearch(name, value){
    let param = URLSearchParams(window.location.search);
    if (param.has(name) && param.get(name) == value){
        param.delete(name);
    }else{
        param.set(name, value);
    }
    window.location.search = param.toString();
}