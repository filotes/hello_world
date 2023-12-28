 
    function run(obj,long,callback){
        clearInterval(obj.timer)
        obj.timer=setInterval(function(){
            if(obj.offsetLeft==long){
                window.clearInterval(obj.timer);
                if(callback){
                    callback();
                }
            }else{
                step=(long-obj.offsetLeft)/10
                step=step>0?Math.ceil(step):Math.floor(step)
                obj.style.left=obj.offsetLeft+step+'px';
            }
        },20)
    }
 
 