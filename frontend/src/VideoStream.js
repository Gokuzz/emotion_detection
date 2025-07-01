import React, { useState } from 'react';
import axios from 'axios';

function VideoStream(){

    const [isStreaming,setIsStreaming] = useState(false);
    const [imgKey,setImgKey] = useState(0);

    const handleToggle = async()=>{

        if(!isStreaming){
            await axios.get('http://localhost:5000/start')
            setIsStreaming(true)
            setImgKey(prev=>prev+1)
        }
        else{
            await   axios.get('http://localhost:5000/stop');
            setIsStreaming(false)
        }

    }

    return(
        <div style={{textAlign:"center"}}>
        <h2>Real-Time Emotion Detection </h2>
        <button onClick={handleToggle} style={{padding:'10px 20px',marginBottom:'20px'}} >{isStreaming ? 'Stop Camera':'Start Camera'}</button>
        {isStreaming && (    
            <div>
            <img key={imgKey} src={`http://localhost:5000/video?ts=${imgKey}`} alt='Emotion stream' style={{width:'600px', border:'2px solid black'}} />
            </div>
        )
        }
        </div>
    )
}

export default VideoStream;