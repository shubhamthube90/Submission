'use client';
import { useEffect, useState } from 'react';

export default function Home() {
  const [docs, setDocs] = useState([]);

  useEffect(() => {
    fetch('http://localhost:8000/documents')
      .then(res => res.json())
      .then(setDocs);
  }, []);

  return (
    <div>
      <h1>Documents</h1>
      {docs.map((doc: any) => (
        <div key={doc.id}>{doc.filename} - {doc.status}</div>
      ))}
    </div>
  );
}
