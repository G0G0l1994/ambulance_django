import { useRef } from "react";
import { Link } from "react-router-dom";
import PatientTab from "./PatientDataTabs";
import TimeDataTab from "./TimeDataTabs";
import CommonDataTab from "./CommonDataTabs";
import ParamsTabs from "./ParamsTabs";
import SkinTabs from "./SkinDataTabs";
import { useCard } from "../hook/useCard";
import {
  Button,
  Tab,
  TabList,
  TabPanel,
  TabPanels,
  Tabs,
} from "@chakra-ui/react";
import { patchCard } from "../endpoints/api";

const CardLayout = ({ card_id }) => {
  const { card, loading, error } = useCard(card_id);
  const patientRef = useRef();
  const timeRef = useRef();
  const commonRef = useRef();
  const paramsBeforeRef = useRef();
  const paramsAfterRef = useRef();
  const skinRef = useRef();

  const handleUpdateCheck = async () => {
    const patientData = patientRef.current?.();
    const timeData = timeRef.current?.();
    const paramsBefore = paramsBeforeRef.current?.();
    const paramsAfter = paramsAfterRef.current?.();
    const skinData = skinRef.current?.();

    const updateData = {
      ...card,
      patient: patientData,
      datetime_data: timeData,
      parameters_before_data: paramsBefore,
      parameters_after_data: paramsAfter,
      skin_data: skinData,
    };
    console.log(updateData);
  };
  const handleSave = async () => {
    try {
      const patientData = patientRef.current?.();
      const timeData = timeRef.current?.();
      const commonData = commonRef.current?.();
      const paramsBefore = paramsBeforeRef.current?.();
      const skinData = skinRef.current?.();
      const updateData = {
        ...card,
        patient: patientData,
        datetime_data: timeData,
        common_data: commonData,
        parameters_before_data: paramsBefore,
        skin_data: skinData,
      };
      await patchCard(card_id, updateData);
      alert("card save");
    } catch (error) {
      console.error("Ошибка сохранения:", error.response?.data);
      alert(
        `Ошибка сохранения: ${error.response?.data?.detail || error.message}`
      );
    }
  };

  if (loading) return <div>Загрузка...</div>;

  return (
    <>
      <Tabs>
        <TabList>
          <Tab>Данные пациента</Tab>
          <Tab>Время</Tab>
          <Tab>Общие данные</Tab>
          <Tab>Параметры до оказания помощи</Tab>
          <Tab>Кожные покровы</Tab>
          <Tab>Дыхательная система</Tab>
          <Tab>Сердечно-сосудистая система</Tab>
          <Tab>Желудочно-кишечный тракт</Tab>
          <Tab>Нервная система</Tab>
          <Tab>Мочевыделительная система</Tab>
          <Tab>ЭКГ</Tab>
          <Tab>Оказанная помощь</Tab>
          <Tab>Параметры после оказания помощи</Tab>
          <Tab>Диагноз</Tab>
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
            <TimeDataTab time={card.datetime_data} onRefSave={timeRef} />
          </TabPanel>
          <TabPanel>
            <CommonDataTab
              common_data={card.common_data}
              onRefSave={commonRef}
            />
          </TabPanel>
          <TabPanel>
            <ParamsTabs
              params={card.parameters_before_data}
              onRefSave={paramsBeforeRef}
            />
          </TabPanel>
          <TabPanel>
            <SkinTabs skin={card.skin_data} onRefSave={skinRef} />
          </TabPanel>
          <TabPanel></TabPanel>
          <TabPanel></TabPanel>
          <TabPanel></TabPanel>
          <TabPanel></TabPanel>
          <TabPanel></TabPanel>
          <TabPanel></TabPanel>
          <TabPanel></TabPanel>
          <TabPanel>
            <ParamsTabs params={card.parameters_after_data} />
          </TabPanel>
          <TabPanel></TabPanel>
        </TabPanels>
      </Tabs>
      <button onClick={handleSave}>Сохранить всё</button>
      <Button onClick={handleUpdateCheck}>
        проверить данные перед отправкой
      </Button>
      <Link to="/dispatcher-main">
        <Button>Назад</Button>
      </Link>
    </>
  );
};

export default CardLayout;
