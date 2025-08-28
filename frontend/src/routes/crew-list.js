import { useState, useEffect } from "react";

import { getCrewList } from "../endpoints/api";

export const CrewList = () => {
  const [crews, setCrews] = useState(null);
  const [loading, setLoading] = useState(true);
  const [errors, setErrors] = useState(null);

  useEffect(() => {
    const fetchCrew = async () => {
      try {
        const crews = await getCrewList();
        if (crews) {
          setCrews(crews);
        } else {
          setErrors("Бригады не найдены");
        }
      } catch (error) {
        setErrors("Ошибка загрузки:" + error.message);
        console.error(error);
      } finally {
        setLoading(false);
      }
    };

    fetchCrew();
  }, []);

  if (loading) return <div>Загрузка...</div>;
  if (errors) return <div>{errors}</div>;
  if (!crews) return <div>Бригады не найдены</div>;

  return (
    <div>
      {crews.map((crew, index) => {
        return (
          <li key={index}>
            Бригада № {crew.crew_number} старший по бригаде: {crew.main_display}{" "}
            фельдшер {crew.secondary_display}<text>   </text>
            <button color="green">Изменить</button>
          </li>
        );
      })}
    </div>
  );
};
