import { useRef } from "react";
import { Link } from "react-router-dom";
import PatientTab from "./Tabs/PatientDataTabs";
import TimeDataTab from "./Tabs/TimeDataTabs";
import CommonDataTab from "./Tabs/CommonDataTabs";
import ParamsTabs from "./Tabs/ParamsTabs";
import SkinTabs from "./Tabs/SkinDataTabs";
import { useCard } from "../hook/useCard";
import AirDataTabs from "./Tabs/AirDataTabs";
import HeartDataTabs from "./Tabs/HeartDataTabs";
import StomachDataTabs from "./Tabs/StomachDataTabs";
import NervousDataTabs from "./Tabs/NervousDataTabs";
import UrinaryDataTabs from "./Tabs/UrinaryDataTabs";
import ECGDataTabs from "./Tabs/ECGDataTabs";
import AidDataTabs from "./Tabs/AidDataTabs";
import DiagnosisDataTabs from "./Tabs/DiagnosisDataTabs";
import { getProfile } from "../endpoints/api";
import { useState, useEffect } from "react";

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
    const [profile, setProfile] = useState({});
    console.log("init card:", card);

    const patientRef = useRef();
    const timeRef = useRef();
    const commonRef = useRef();
    const paramsBeforeRef = useRef();
    const paramsAfterRef = useRef();
    const skinRef = useRef();
    const airRef = useRef();
    const heartRef = useRef();
    const stomachRef = useRef();
    const nervousRef = useRef();
    const urinaryRef = useRef();
    const ecgRef = useRef();
    const aidRef = useRef();
    const diagnosisRef = useRef();
    useEffect(() => {
        const fetchProfile = async () => {
            const data = await getProfile();
            setProfile(data);
        };
        fetchProfile();
    }, []);
    console.log(profile);
    const handleSave = async () => {
        try {
            // Получаем данные из всех табов
            console.log("Извлечение данных из ref...");
            const patientDataRaw = patientRef.current?.();
            console.log("patientDataRaw:", patientDataRaw);
            // Извлекаем адрес из данных пациента (если он там есть)
            const { _address, ...patientData } = patientDataRaw || {};

            const timeData = timeRef.current?.();
            console.log("timeData:", timeData);
            const commonData = commonRef.current?.();
            console.log("commonData:", commonData);
            const paramsBefore = paramsBeforeRef.current?.();
            console.log("paramsBefore:", paramsBefore);
            const skinData = skinRef.current?.();
            console.log("skinData:", skinData);
            const airData = airRef.current?.();
            console.log("airData:", airData);
            const heartData = heartRef.current?.();
            console.log("heartData:", heartData);
            const stomachData = stomachRef.current?.();
            console.log("stomachData:", stomachData);
            const nervousData = nervousRef.current?.();
            console.log("nervousData:", nervousData);
            const urinaryData = urinaryRef.current?.();
            console.log("urinaryData:", urinaryData);
            const ecgData = ecgRef.current?.();
            console.log("ecgData:", ecgData);
            const aidData = aidRef.current?.();
            console.log("aidData:", aidData);
            const paramsAfter = paramsAfterRef.current?.();
            console.log("paramsAfter:", paramsAfter);
            const diagnosisData = diagnosisRef.current?.();
            console.log("diagnosisData:", diagnosisData);

            // Функция для проверки, что объект не пустой и содержит данные
            const hasData = (obj) => {
                if (!obj || typeof obj !== "object") return false;
                // Проверяем, что есть хотя бы одно поле (включая id, так как id может быть важен)
                const keys = Object.keys(obj);
                return keys.length > 0;
            };

            const updateData = {
                // Не копируем весь card, чтобы не отправлять лишние данные
                doctor_id: profile.id || card.doctor_id,
                address: _address !== undefined ? _address : card.address, // Используем адрес из PatientTab или текущий
                crew: card.crew,
                cause: card.cause,
                status: card.status,
            };

            // Добавляем данные только если они не пустые
            if (hasData(patientData)) {
                updateData.patient = patientData;
            }
            if (hasData(timeData)) {
                updateData.datetime_data = timeData;
            }
            if (hasData(commonData)) {
                updateData.common_data = commonData;
            }
            if (hasData(paramsBefore)) {
                updateData.parameters_before_data = paramsBefore;
            }
            if (hasData(skinData)) {
                updateData.skin_data = skinData;
            }
            if (hasData(airData)) {
                updateData.air_data = airData;
            }
            if (hasData(heartData)) {
                updateData.heart_data = heartData;
            }
            if (hasData(stomachData)) {
                updateData.stomach_data = stomachData;
            }
            if (hasData(nervousData)) {
                updateData.nervous_data = nervousData;
            }
            if (hasData(urinaryData)) {
                updateData.urinary_data = urinaryData;
            }
            if (hasData(ecgData)) {
                updateData.ecg_data = ecgData;
            }
            if (hasData(aidData)) {
                updateData.aid_data = aidData;
            }
            if (hasData(paramsAfter)) {
                updateData.parameters_after_data = paramsAfter;
            }
            if (hasData(diagnosisData)) {
                updateData.diagnosis_data = diagnosisData;
            }

            console.log("Отправляемые данные:", updateData);
            await patchCard(card_id, updateData);
            alert("Карта сохранена");
        } catch (error) {
            console.error("Ошибка сохранения:", error.response?.data);
            alert(
                `Ошибка сохранения: ${
                    error.response?.data?.detail || error.message
                }`
            );
        }
    };

    if (loading) return <div>Загрузка...</div>;

    return (
        <>
            <Tabs>
                <TabList overflowX="auto" overflowY="hidden">
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
                        <TimeDataTab
                            time={card.datetime_data}
                            onRefSave={timeRef}
                        />
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
                    <TabPanel>
                        <AirDataTabs air={card.air_data} onRefSave={airRef} />
                    </TabPanel>
                    <TabPanel>
                        <HeartDataTabs
                            heart={card.heart_data}
                            onRefSave={heartRef}
                        />
                    </TabPanel>
                    <TabPanel>
                        <StomachDataTabs
                            stomach={card.stomach_data}
                            onRefSave={stomachRef}
                        />
                    </TabPanel>
                    <TabPanel>
                        <NervousDataTabs
                            nervous={card.nervous_data}
                            onRefSave={nervousRef}
                        />
                    </TabPanel>
                    <TabPanel>
                        <UrinaryDataTabs
                            urinary={card.urinary_data}
                            onRefSave={urinaryRef}
                        />
                    </TabPanel>
                    <TabPanel>
                        <ECGDataTabs ecg={card.ecg_data} onRefSave={ecgRef} />
                    </TabPanel>
                    <TabPanel>
                        <AidDataTabs
                            aid_data={card.aid_data}
                            onRefSave={aidRef}
                        />
                    </TabPanel>
                    <TabPanel>
                        <ParamsTabs
                            params={card.parameters_after_data}
                            onRefSave={paramsAfterRef}
                        />
                    </TabPanel>
                    <TabPanel>
                        <DiagnosisDataTabs
                            diagnosis={card.diagnosis_data}
                            onRefSave={diagnosisRef}
                        />
                    </TabPanel>
                </TabPanels>
            </Tabs>
            <button onClick={handleSave}>Сохранить всё</button>

            <Link to="/dispatcher-main">
                <Button>Назад</Button>
            </Link>
        </>
    );
};

export default CardLayout;
