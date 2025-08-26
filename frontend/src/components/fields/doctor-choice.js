import { useState } from "react";
import { Select, Button } from "@chakra-ui/react";
import { patchCard, getCard } from "../../endpoints/api";

export const DoctorChoice = ({ doctors, card, onDoctorAssigned }) => {
  const [selectedDoctorId, setSelectedDoctorId] = useState("");
  const [isLoading, setIsLoading] = useState(false);

  const handleAssignDoctor = async () => {
    if (!selectedDoctorId) {
      alert("Пожалуйста, выберите врача");
      return;
    }

    setIsLoading(true);
    try {
      await patchCard(card.id, {
        doctor_id: Number(selectedDoctorId),
      });
      alert("Врач успешно назначен");
      setSelectedDoctorId(""); // Сбросить выбор после успешного назначения
      // Можно добавить callback для обновления родительского состояния

      if (onDoctorAssigned) {
        onDoctorAssigned();
      }
    } catch (error) {
      console.error("Ошибка назначения врача:", error);
      alert("Ошибка при назначении врача");
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <>
      <Select
        placeholder="Назначить врача"
        value={selectedDoctorId}
        onChange={(e) => setSelectedDoctorId(e.target.value)}
        disabled={isLoading}
      >
        {doctors.map((doc) => (
          <option key={doc.id} value={doc.id}>
            {doc.first_name} {doc.last_name}
          </option>
        ))}
      </Select>
      <Button
        onClick={handleAssignDoctor}
        isLoading={isLoading}
        ml={2}
        disabled={!selectedDoctorId}
      >
        Назначить
      </Button>
    </>
  );
};
