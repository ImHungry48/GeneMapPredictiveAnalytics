import React, { useCallback, useState } from 'react';
import '../styles/Dropzone.css'

const DropZone = () => {
  const [dragging, setDragging] = useState(false);

  const handleDragIn = useCallback((e) => {
    e.preventDefault();
    e.stopPropagation();
  }, []);

  const handleDragOut = useCallback((e) => {
    e.preventDefault();
    e.stopPropagation();
    setDragging(false);
  }, []);

  const handleDragOver = useCallback((e) => {
    e.preventDefault();
    e.stopPropagation();

    if (e.dataTransfer.items && e.dataTransfer.items.length > 0) {
      setDragging(true);
    }
  }, []);

  const handleDrop = useCallback((e) => {
    e.preventDefault();
    e.stopPropagation();
    setDragging(false);

    if (e.dataTransfer.files && e.dataTransfer.files.length > 0) {
      // TODO: Handle file upload process here
      console.log(e.dataTransfer.files);
      e.dataTransfer.clearData();
    }
  }, []);

  return (
    <div
      className={`dropzone ${dragging ? 'active' : ''}`}
      onDrop={handleDrop}
      onDragOver={handleDragOver}
      onDragEnter={handleDragIn}
      onDragLeave={handleDragOut}
    >
      {dragging ?
        <div className="drop-message">Drop the files here ...</div> :
        <div className="drop-message">Drop genome here</div>
      }
    </div>
  );
};

export default DropZone;
