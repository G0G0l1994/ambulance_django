import { useRef } from "react";
import PatientTab from "./PatientDataTabs";
import TimeDataTab from "./TimeDataTabs";
import { useCard } from "../hook/useCard";
import { Tab, TabList, TabPanel, TabPanels, Tabs } from "@chakra-ui/react";

const CardLayout = ({ card_id }) => {
  const { card, loading, error } = useCard(card_id);
  const patientRef = useRef();
  const timeRef = useRef();

  const handleSave = () => {
    const patientData = patientRef.current?.();
    const timeData = timeRef.current?.();
    console.log("Отправляем на сервер:", {
      ...card,
      patient: patientData,
      datetime_data: timeData,
    });
    console.log(
      new Date(card.patient.date_of_birth || " ").toLocaleDateString("ru-ru")
    );
    // await saveData(...)
  };

  if (loading) return <div>Загрузка...</div>;

  return (
    <>
      <Tabs>
        <TabList>
          <Tab>Данные пациента</Tab>
          <Tab>Время</Tab>
        </TabList>
        <TabPanels>
          <TabPanel>
            <PatientTab
              patient={card.patient}
              onSaveRef={patientRef}
              address={card.address}
            />
          </TabPanel>
          <TabPanel>
            <TimeDataTab time={card.datetime_data} onSaveRef={timeRef} />
          </TabPanel>
        </TabPanels>
      </Tabs>
      <button onClick={handleSave}>Сохранить всё</button>
    </>
  );
};

export default CardLayout;
