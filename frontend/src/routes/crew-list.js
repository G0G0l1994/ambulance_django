import { useState, useEffect } from "react";
import { SelectChoice } from "../components/fields/choice.field";
import { getCrewList, getDoctorsList, updateCrew } from "../endpoints/api";
import { HStack, Text, Box, Button, VStack } from "@chakra-ui/react";

export const CrewList = () => {
  const [crews, setCrews] = useState([]);
  const [doctors, setDoctors] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [saving, setSaving] = useState({}); // Состояние для отслеживания сохранения каждой бригады

  useEffect(() => {
    const fetchData = async () => {
      try {
        const [crewsData, doctorsData] = await Promise.all([
          getCrewList(),
          getDoctorsList(),
        ]);

        setCrews(crewsData || []);

        // Преобразуем врачей в формат для Select
        const doctorOptions = (doctorsData || []).map((doctor) => ({
          value: doctor.id,
          name:
            doctor.full_name_display ||
            `${doctor.first_name} ${doctor.surname || ""} ${doctor.last_name}`,
        }));
        setDoctors(doctorOptions);
      } catch (err) {
        setError("Ошибка загрузки: " + err.message);
        console.error(err);
      } finally {
        setLoading(false);
      }
    };

    fetchData();
  }, []);

  const handleCrewChange = (crewId, field, value) => {
    // Обновляем локальное состояние
    const updatedCrews = crews.map((crew) =>
      crew.id === crewId ? { ...crew, [field]: parseInt(value) } : crew
    );
    setCrews(updatedCrews);
  };

  const saveCrewChanges = async (crewId) => {
    setSaving((prev) => ({ ...prev, [crewId]: true }));

    try {
      const crewToUpdate = crews.find((crew) => crew.id === crewId);
      if (!crewToUpdate) return;

      // Отправляем изменения на сервер
      await updateCrew(crewId, {
        main: crewToUpdate.main,
        secondary: crewToUpdate.secondary,
      });

      // Обновляем UI после успешного сохранения
      setError(null);
      alert(`Бригада обновлена`);
    } catch (err) {
      setError("Ошибка сохранения: " + err.message);
      console.error(err);
    } finally {
      setSaving((prev) => ({ ...prev, [crewId]: false }));
    }
  };

  if (loading) return <div>Загрузка...</div>;
  if (error) return <div>{error}</div>;

  return (
    <Box>
      {crews.map((crew) => (
        <VStack
          key={crew.id}
          spacing={4}
          p={4}
          borderWidth={1}
          borderRadius="md"
          mb={4}
          align="start"
        >
          <Text fontWeight="bold">Бригада №{crew.crew_number}</Text>

          <HStack spacing={4} wrap="wrap">
            <SelectChoice
              fieldname="Доктор/Фельдшер:"
              options={doctors}
              defaultValue={crew.main}
              onChange={(e) =>
                handleCrewChange(crew.id, "main", e.target.value)
              }
            />

            <SelectChoice
              fieldname="Фельдшер:"
              options={doctors}
              defaultValue={crew.secondary}
              onChange={(e) =>
                handleCrewChange(crew.id, "secondary", e.target.value)
              }
            />

            <Button
              colorScheme="blue"
              onClick={() => saveCrewChanges(crew.id)}
              isLoading={saving[crew.id]}
              loadingText="Сохранение"
            >
              Сохранить
            </Button>
          </HStack>
        </VStack>
      ))}
    </Box>
  );
};
