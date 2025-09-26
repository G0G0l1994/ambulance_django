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
            const patientData = patientRef.current?.();
            const timeData = timeRef.current?.();
            const commonData = commonRef.current?.();
            const paramsBefore = paramsBeforeRef.current?.();
            const skinData = skinRef.current?.();
            const airData = airRef.current?.();
            const heartData = heartRef.current?.();
            const stomachData = stomachRef.current?.();
            const nervousData = nervousRef.current?.();
            const urinaryData = urinaryRef.current?.();
            const ecgData = ecgRef.current?.();
            const aidData = aidRef.current?.();
            const paramsAfter = paramsAfterRef.current?.();
            const diagnosisData = diagnosisRef.current?.();

            const updateData = {
                ...card,
                doctor_id: profile.id,
                patient: patientData,
                datetime_data: timeData,
                common_data: commonData,
                parameters_before_data: paramsBefore,
                skin_data: skinData,
                air_data: airData,
                heart_data: heartData,
                stomach_data: stomachData,
                nervous_data: nervousData,
                urinary_data: urinaryData,
                ecg_data: ecgData,
                aid_data: aidData,
                parameters_after_data: paramsAfter,
                diagnosis_data: diagnosisData,
            };
            console.log(updateData);
            await patchCard(card_id, updateData);
            alert("card save");
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
