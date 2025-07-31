import React, { useState } from 'react';

function App() {
  const [repoUrl, setRepoUrl] = useState('');
  const [domain, setDomain] = useState('');
  const [logo, setLogo] = useState(null);
  const [status, setStatus] = useState('');

  const handleDeploy = async () => {
    const formData = new FormData();
    formData.append("repo_url", repoUrl);
    formData.append("domain", domain);
    if (logo) formData.append("logo", logo);

    const response = await fetch("https://app-builder-backend.onrender.com/deploy/", {
      method: "POST",
      body: formData,
    });

    const result = await response.json();
    setStatus(result.message);
  };

  return (
    <div style={{ padding: "20px" }}>
      <h1>🚀 Launch Your App</h1>
      <input placeholder="GitHub Repo URL" onChange={(e) => setRepoUrl(e.target.value)} />
      <br /><br />
      <input placeholder="yourdomain.com" onChange={(e) => setDomain(e.target.value)} />
      <br /><br />
      <input type="file" onChange={(e) => setLogo(e.target.files[0])} />
      <br /><br />
      <button onClick={handleDeploy}>Deploy Now</button>
      <p>{status}</p>
    </div>
  );
}

export default App;
