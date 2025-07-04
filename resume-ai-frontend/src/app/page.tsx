"use client";

import { useState } from "react";
import { useDropzone } from "react-dropzone";

export default function Home() {
  const [file, setFile] = useState<File | null>(null);
  const [jobDesc, setJobDesc] = useState("");
  const [loading, setLoading] = useState(false);
  const [resumePdfUrl, setResumePdfUrl] = useState<string | null>(null);
  const [coverPdfUrl, setCoverPdfUrl] = useState<string | null>(null);
  const [error, setError] = useState<string | null>(null);
  const [progress, setProgress] = useState<string | null>(null);

  const onDrop = (acceptedFiles: File[]) => {
    setFile(acceptedFiles[0]);
  };

  const { getRootProps, getInputProps, isDragActive } = useDropzone({
    onDrop,
    accept: {
      "application/pdf": [".pdf"],
      "application/vnd.openxmlformats-officedocument.wordprocessingml.document": [".docx"],
    },
    multiple: false,
  });

  const handleGenerate = async () => {
    if (!file || !jobDesc) return;

    setError(null);
    setLoading(true);
    setResumePdfUrl(null);
    setCoverPdfUrl(null);

    const formData = new FormData();
    formData.append("resume", file);
    formData.append("job_description", jobDesc);

    try {
      setProgress("Generating Resume...");
      const resumeRes = await fetch("http://localhost:8080/api/resume/", {
        method: "POST",
        body: formData,
      });

      if (!resumeRes.ok) {
        const errorText = await resumeRes.text();
        throw new Error(errorText || "Resume generation failed");
      }

      const resumeBlob = await resumeRes.blob();
      setResumePdfUrl(URL.createObjectURL(resumeBlob));

      setProgress("Generating Cover Letter...");
      const coverRes = await fetch("http://localhost:8080/api/cover/", {
        method: "POST",
        body: formData,
      });

      if (!coverRes.ok) {
        const errorText = await coverRes.text();
        throw new Error(errorText || "Cover letter generation failed");
      }

      const coverBlob = await coverRes.blob();
      setCoverPdfUrl(URL.createObjectURL(coverBlob));

      setProgress("Rendering PDFs...");
    } catch (error) {
      console.error("Error generating documents:", error);
      setError("Failed to generate documents. Please try again.");
    } finally {
      setLoading(false);
      setProgress(null);
    }
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-purple-900 to-black text-white flex flex-col items-center justify-center px-6 py-12">
      <div className="max-w-3xl w-full bg-white/10 backdrop-blur-lg p-8 rounded-2xl shadow-lg space-y-6">
        <h1 className="text-4xl font-bold text-center">✨ Resume Tailor AI</h1>
        <p className="text-center text-lg text-white/80">
          Upload your resume and paste a job description. Let AI tailor it for you.
        </p>

        <div
          {...getRootProps()}
          className={`w-full p-6 border-2 border-dashed rounded cursor-pointer ${
            isDragActive ? "border-purple-400 bg-white/20" : "border-white/20 bg-white/10"
          } text-white text-center`}>
          <input {...getInputProps()} />
          {file ? (
            <p>{file.name}</p>
          ) : (
            <p>Drag and drop your resume here, or click to select a PDF/DOCX file</p>
          )}
        </div>

        <div>
          <label className="block mb-2 text-sm font-medium">Paste Job Description</label>
          <textarea
            rows={6}
            value={jobDesc}
            onChange={e => setJobDesc(e.target.value)}
            placeholder="Enter job description here..."
            className="w-full bg-white/10 border border-white/20 text-white p-3 rounded"
          />
        </div>

        <button
          onClick={handleGenerate}
          disabled={loading}
          className="w-full bg-purple-700 hover:bg-purple-800 py-3 rounded text-white font-semibold disabled:opacity-50">
          {loading ? "Generating..." : "Generate Resume and Cover Letter"}
        </button>

        {progress && <div className="text-center text-sm text-purple-300 mt-2">{progress}</div>}

        {resumePdfUrl && (
          <div className="text-center mt-4">
            <a
              href={resumePdfUrl}
              target="_blank"
              rel="noopener noreferrer"
              className="underline text-purple-300">
              🔗 View Your Tailored Resume
            </a>
          </div>
        )}

        {coverPdfUrl && (
          <div className="text-center mt-2">
            <a
              href={coverPdfUrl}
              target="_blank"
              rel="noopener noreferrer"
              className="underline text-purple-300">
              ✉️ View Your Cover Letter
            </a>
          </div>
        )}

        {error && <div className="text-center text-red-400 mt-4">⚠️ {error}</div>}
      </div>
    </div>
  );
}
