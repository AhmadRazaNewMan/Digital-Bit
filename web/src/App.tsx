import { Route, Routes } from "react-router-dom";
import { Layout } from "./components/Layout";
import { Home } from "./pages/Home";
import { PostPage } from "./pages/PostPage";

export default function App() {
  return (
    <Layout>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/post/:moduleId/:postId" element={<PostPage />} />
      </Routes>
    </Layout>
  );
}
