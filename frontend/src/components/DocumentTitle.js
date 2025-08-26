import { useEffect, useState } from "react";

import { getProfile } from "../endpoints/api";

const DocumentTitle = () => {
    const [profile, setProfile] = useState(null)
    
    useEffect(() => {
        const fetchProfile = async () => {
            const data = await getProfile();
            setProfile(data);
        };
        fetchProfile();
    }, []);
  useEffect(() => {
    if (profile && profile.username) {
      document.title = `${profile.username} - Медицинская система`;
    } else {
      document.title = "Медицинская система";
    }
  }, [profile]);

  return null;
};

export default DocumentTitle;
