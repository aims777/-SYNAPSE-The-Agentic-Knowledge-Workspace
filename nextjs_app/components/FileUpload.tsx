"use client";

import { useState } from 'react';
import axios from 'axios';
import toast from 'react-hot-toast';

export default function FileUpload() {
  const [file, setFile] = useState<File | null>(null);
  const [uploading, setUploading] = useState(false);

  const handleFileChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    if (e.target.files) {
      setFile(e.target.files[0]);
    }
  };

  const handleUpload = async () => {
    if (!file) {
      toast.error('Please select a file to upload.');
      return;
    }

    setUploading(true);
    const formData = new FormData();
    formData.append('file', file);

    try {
      const response = await axios.post('http://localhost:8000/upload', formData, {
        headers: {
          'Content-Type': 'multipart/form-data',
        },
      });
      toast.success(response.data.message);
    } catch (error) {
      toast.error('Error uploading file.');
    }

    setUploading(false);
  };

  return (
    <div className="w-full p-4 border rounded-lg">
      <h2 className="text-2xl font-bold mb-4">Upload Document</h2>
      <div className="flex items-center space-x-4">
        <input type="file" onChange={handleFileChange} className="flex-grow" />
        <button onClick={handleUpload} disabled={uploading} className="px-4 py-2 bg-blue-500 text-white rounded-lg disabled:bg-gray-400">
          {uploading ? 'Uploading...' : 'Upload'}
        </button>
      </div>
    </div>
  );
}
