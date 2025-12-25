import { useEffect, useState } from "react";
import {
  HStack,
  Input,
  Text,
  VStack,
  Grid,
  GridItem,
  Button,
} from "@chakra-ui/react";

const TimeDataTab = ({ time, onRefSave }) => {
  const [localData, setLocalData] = useState(time);
  useEffect(() => {
    setLocalData(time);
  }, [time]);

  const handleChange = (field, value) => {
    setLocalData((prev) => ({ ...prev, [field]: value }));
  };

  useEffect(() => {
    if (onRefSave) {
      onRefSave.current = () => localData || {};
    }
  }, [localData, onRefSave]);
  return (
    <Grid gap={5} templateColumns="repeat(2, 1fr)">
      <GridItem columnGap={1}>
        <HStack>
          <Text>Время приёма:</Text>
          <Input
            value={new Date(
              localData?.time_of_receipt || ""
            ).toLocaleTimeString("ru-ru")}
            onChange={(e) => handleChange("time_of_receipt", e.target.value)}
          />
        </HStack>
        <HStack>
          <Text>Время передачи:</Text>
          <Input
            value={new Date(localData?.transmission_time).toLocaleTimeString(
              "ru-ru"
            )}
            onChange={(e) => handleChange("transmission_time", e.target.value)}
          />
        </HStack>
        <HStack>
          <Text>Время принятия бригадой:</Text>
          <Input
            value={new Date(
              localData?.departure_time || " "
            ).toLocaleTimeString("ru-ru")}
            onChange={(e) => handleChange("departure_time", e.target.value)}
          />
        </HStack>
        <HStack>
          <Text>Время прибытия:</Text>
          {localData.arrival_time && (
            <Input
              value={new Date(localData.arrival_time || " ").toLocaleTimeString(
                "ru-ru"
              )}
              onChange={(e) => {
                handleChange("arrival_time", e.target.value);
              }}
            />
          )}
          {!localData.arrival_time && (
            <Button
              backgroundColor="blue.300"
              onClick={(e) => {
                handleChange(
                  "arrival_time",
                  new Date(Date.now()).toISOString()
                );
              }}
            >
              Отметить
            </Button>
          )}
        </HStack>
      </GridItem>
      <GridItem>
        <HStack>
          <Text>Начало госпитализации:</Text>

          {localData.start_time_of_hospitalization && (
            <Input
              value={
                localData.start_time_of_hospitalization
                  ? new Date(
                      localData.start_time_of_hospitalization
                    ).toLocaleTimeString("ru-ru")
                  : "00:00:00"
              }
              onChange={(e) => {
                handleChange("start_time_of_hospitalization", e.target.value);
              }}
            />
          )}
          {!localData.start_time_of_hospitalization && (
            <Button
              backgroundColor="blue.300"
              onClick={(e) => {
                handleChange(
                  "start_time_of_hospitalization",
                  new Date(Date.now()).toISOString()
                );
              }}
            >
              {" "}
              Отметить
            </Button>
          )}
        </HStack>
        <HStack>
          <Text>Время прибытия в стационар:</Text>
          {localData.time_of_arrival_at_hospital && (
            <Input
              value={
                localData.time_of_arrival_at_hospital
                  ? new Date(
                      localData.time_of_arrival_at_hospital
                    ).toLocaleTimeString("ru-ru")
                  : "00:00:00"
              }
              onChange={(e) => {
                handleChange("time_of_arrival_at_hospital", e.target.value);
              }}
            />
          )}
          {!localData.time_of_arrival_at_hospital && (
            <Button
              backgroundColor="blue.300"
              onClick={(e) => {
                handleChange(
                  "time_of_arrival_at_hospital",
                  new Date(Date.now()).toISOString()
                );
              }}
            >
              {" "}
              Отметить
            </Button>
          )}
        </HStack>
        <HStack>
          <Text>Окончание вызова:</Text>
          {localData.call_end_time && (
            <Input
              value={new Date(
                localData.call_end_time || " "
              ).toLocaleTimeString("ru-ru")}
              onChange={(e) => handleChange("call_end_time", e.target.value)}
            />
          )}
          {!localData.call_end_time && (
            <Button
              backgroundColor="blue.300"
              onClick={(e) => {
                handleChange(
                  "call_end_time",
                  new Date(Date.now()).toISOString()
                );
              }}
            >
              Отметить
            </Button>
          )}
        </HStack>
      </GridItem>
    </Grid>
  );
};

export default TimeDataTab;
