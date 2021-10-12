<?xml version="1.0" encoding="ASCII"?>
<byteblowerguimodel_v1_3:ByteBlowerProject xmi:version="2.0" xmlns:xmi="http://www.omg.org/XMI" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:byteblowerguimodel_v1_3="http:///com.excentis.products.byteblower.gui.model.ecore" name="NAT" author="pieter.v" modelVersion="2.9.2" defaultBatchInitializationTime="10000000000" warningLossLevel="0.01" errorLossLevel="0.02" reportOutputToHtml="true" reportOutputToExcel="false" reportOutputToCsv="true" reportProjectBackup="true" throughputUnit="kbps" scenarioIdenticalFramesWarning="true" scenarioPauseAfterDhcp="true" scenarioEnableScoutingFrames="true" scenarioIgnoreInitializationErrors="false" scenarioWaitTimeAfterScenario="5000000000" throughputType="FrameOnly" dhcpTimeout="1000000000" numberOfDecimals="2" dhcpRetries="5" latencyRangeStart="0" latencyRangeEnd="100000000" latencyUnit="17" numberOfLatencyDecimals="3" reportOutputToPdf="false" ScenarioHttpAllowAlive="9223372036854775807" scenarioAutomaticTcpRestart="true">
  <Scenario name="Ex 1 Basic Nat">
    <measurements xsi:type="byteblowerguimodel_v1_3:FlowMeasurement" flow="//@Flow.0">
      <flowStartEvent scheduledTime="0"/>
      <flowStopEvent scheduledTime="10000000000"/>
    </measurements>
  </Scenario>
  <Scenario name="Ex 2 Force remap">
    <measurements xsi:type="byteblowerguimodel_v1_3:FlowMeasurement" flow="//@Flow.0">
      <flowStartEvent scheduledTime="0"/>
      <flowStopEvent scheduledTime="10000000000"/>
    </measurements>
    <measurements xsi:type="byteblowerguimodel_v1_3:FlowMeasurement" flow="//@Flow.1">
      <flowStartEvent scheduledTime="0"/>
      <flowStopEvent scheduledTime="10000000000"/>
    </measurements>
  </Scenario>
  <Scenario name="Ex 3 NAT timeout check">
    <measurements xsi:type="byteblowerguimodel_v1_3:FlowMeasurement" flow="//@Flow.0">
      <flowStartEvent scheduledTime="0"/>
      <flowStopEvent scheduledTime="1800000000000"/>
    </measurements>
  </Scenario>
  <Scenario name="Ex 4 Blocked traffic">
    <measurements xsi:type="byteblowerguimodel_v1_3:FlowMeasurement" flow="//@Flow.2">
      <flowStartEvent scheduledTime="0"/>
      <flowStopEvent scheduledTime="10000000000"/>
    </measurements>
  </Scenario>
  <Flow name="Default Template" source="//@ByteBlowerGuiPort.0" destination="//@ByteBlowerGuiPort.1" FlowTemplate="//@FlowTemplate.0" latencyAndJitterType="No" flowMeasurement="//@Scenario.0/@measurements.0 //@Scenario.1/@measurements.0 //@Scenario.2/@measurements.0" tos="0"/>
  <Flow name="Same Template" source="//@ByteBlowerGuiPort.0" destination="//@ByteBlowerGuiPort.2" FlowTemplate="//@FlowTemplate.0" latencyAndJitterType="No" flowMeasurement="//@Scenario.1/@measurements.1" tos="0"/>
  <Flow name="Blocked Traffic" source="//@ByteBlowerGuiPort.0" destination="//@ByteBlowerGuiPort.3" FlowTemplate="//@FlowTemplate.0" latencyAndJitterType="No" flowMeasurement="//@Scenario.3/@measurements.0" tos="0"/>
  <FlowTemplate xsi:type="byteblowerguimodel_v1_3:FrameBlastingFlow" name="FRAME_BLASTING_1" Flow="//@Flow.0 //@Flow.1 //@Flow.2" frameInterval="10000000" dataRateUnit="kbps">
    <frameBlastingFrames weight="1" frame="//@Frame.0"/>
  </FlowTemplate>
  <Frame name="FRAME_1" bytesHexString="0000000000000000000000000800450003F202780000FE11B27F01010101010101011000100003DECCC9457863656E7469732042797465426C6F7765722044656661756C74205061796C6F61642E00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000" L2AutoSourceMac="true" L2AutoDestMac="true" L3AutoSourceIp="true" L3AutoDestIp="true" L3AutoHeaderCheck="true" L3AutoTotLen="true" L3LinkWithL2="true" L4AutoTcpChecksum="false" L4AutoUdpChecksum="true" L4AutoTotLen="true" L4LinkWithL3="true" L3AutoArpSHA="false" L3AutoArpSPA="false" L3AutoArpTHA="false" L3AutoArpTPA="false" L3AutoIpv6Source="false" L3AutoIpv6Destination="false" L3AutoIpv6PayloadLength="false" frameBlastingFrames="//@FlowTemplate.0/@frameBlastingFrames.0" L4AllowPortOverride="true">
    <modifiers xsi:type="byteblowerguimodel_v1_3:UniqueFieldModifier" fieldLength="1" offset="0"/>
  </Frame>
  <ByteBlowerGuiPort name="WAN" theSourceOfFlow="//@Flow.0 //@Flow.1 //@Flow.2" natted="false" mtu="1500">
    <layer2Configuration xsi:type="byteblowerguimodel_v1_3:EthernetConfiguration">
      <MacAddress>
        <bytes>0</bytes>
        <bytes>-1</bytes>
        <bytes>-69</bytes>
        <bytes>-51</bytes>
        <bytes>0</bytes>
        <bytes>1</bytes>
      </MacAddress>
    </layer2Configuration>
    <ipv4Configuration isActive="true" addressConfiguration="DHCPv4" dhcpOptions="//@Dhcp.0">
      <IpAddress>
        <bytes>0</bytes>
        <bytes>0</bytes>
        <bytes>0</bytes>
        <bytes>0</bytes>
      </IpAddress>
      <Netmask>
        <bytes>-1</bytes>
        <bytes>-1</bytes>
        <bytes>-1</bytes>
        <bytes>0</bytes>
      </Netmask>
      <DefaultGateway>
        <bytes>0</bytes>
        <bytes>0</bytes>
        <bytes>0</bytes>
        <bytes>0</bytes>
      </DefaultGateway>
    </ipv4Configuration>
    <ipv6Configuration isActive="false" addressConfiguration="Fixed" prefixLength="64">
      <IpAddress>
        <bytes>0</bytes>
        <bytes>0</bytes>
        <bytes>0</bytes>
        <bytes>0</bytes>
        <bytes>0</bytes>
        <bytes>0</bytes>
        <bytes>0</bytes>
        <bytes>0</bytes>
        <bytes>0</bytes>
        <bytes>0</bytes>
        <bytes>0</bytes>
        <bytes>0</bytes>
        <bytes>0</bytes>
        <bytes>0</bytes>
        <bytes>0</bytes>
        <bytes>0</bytes>
      </IpAddress>
      <DefaultRouter>
        <bytes>0</bytes>
        <bytes>0</bytes>
        <bytes>0</bytes>
        <bytes>0</bytes>
        <bytes>0</bytes>
        <bytes>0</bytes>
        <bytes>0</bytes>
        <bytes>0</bytes>
        <bytes>0</bytes>
        <bytes>0</bytes>
        <bytes>0</bytes>
        <bytes>0</bytes>
        <bytes>0</bytes>
        <bytes>0</bytes>
        <bytes>0</bytes>
        <bytes>0</bytes>
      </DefaultRouter>
    </ipv6Configuration>
    <ByteBlowerGuiPortConfiguration physicalServerAddress="byteblower-tutorial-1300.lab.byteblower.excentis.com" physicalInterfaceId="1" physicalPortId="-1" physicalServerType="ByteBlower"/>
  </ByteBlowerGuiPort>
  <ByteBlowerGuiPort name="Behind NAT_1" theDestinationOfFlow="//@Flow.0" natted="true" mtu="1500">
    <layer2Configuration xsi:type="byteblowerguimodel_v1_3:EthernetConfiguration">
      <MacAddress>
        <bytes>0</bytes>
        <bytes>-1</bytes>
        <bytes>-69</bytes>
        <bytes>-51</bytes>
        <bytes>0</bytes>
        <bytes>2</bytes>
      </MacAddress>
    </layer2Configuration>
    <ipv4Configuration isActive="true" addressConfiguration="DHCPv4" dhcpOptions="//@Dhcp.0">
      <IpAddress>
        <bytes>0</bytes>
        <bytes>0</bytes>
        <bytes>0</bytes>
        <bytes>0</bytes>
      </IpAddress>
      <Netmask>
        <bytes>-1</bytes>
        <bytes>-1</bytes>
        <bytes>-1</bytes>
        <bytes>0</bytes>
      </Netmask>
      <DefaultGateway>
        <bytes>0</bytes>
        <bytes>0</bytes>
        <bytes>0</bytes>
        <bytes>0</bytes>
      </DefaultGateway>
    </ipv4Configuration>
    <ipv6Configuration isActive="false" addressConfiguration="Fixed" prefixLength="64">
      <IpAddress>
        <bytes>0</bytes>
        <bytes>0</bytes>
        <bytes>0</bytes>
        <bytes>0</bytes>
        <bytes>0</bytes>
        <bytes>0</bytes>
        <bytes>0</bytes>
        <bytes>0</bytes>
        <bytes>0</bytes>
        <bytes>0</bytes>
        <bytes>0</bytes>
        <bytes>0</bytes>
        <bytes>0</bytes>
        <bytes>0</bytes>
        <bytes>0</bytes>
        <bytes>0</bytes>
      </IpAddress>
      <DefaultRouter>
        <bytes>0</bytes>
        <bytes>0</bytes>
        <bytes>0</bytes>
        <bytes>0</bytes>
        <bytes>0</bytes>
        <bytes>0</bytes>
        <bytes>0</bytes>
        <bytes>0</bytes>
        <bytes>0</bytes>
        <bytes>0</bytes>
        <bytes>0</bytes>
        <bytes>0</bytes>
        <bytes>0</bytes>
        <bytes>0</bytes>
        <bytes>0</bytes>
        <bytes>0</bytes>
      </DefaultRouter>
    </ipv6Configuration>
    <ByteBlowerGuiPortConfiguration physicalServerAddress="byteblower-tutorial-1300.lab.byteblower.excentis.com" physicalInterfaceId="0" physicalPortId="44" physicalServerType="ByteBlower"/>
  </ByteBlowerGuiPort>
  <ByteBlowerGuiPort name="Behind NAT_2" theDestinationOfFlow="//@Flow.1" natted="true" mtu="1500">
    <layer2Configuration xsi:type="byteblowerguimodel_v1_3:EthernetConfiguration">
      <MacAddress>
        <bytes>0</bytes>
        <bytes>-1</bytes>
        <bytes>-69</bytes>
        <bytes>-51</bytes>
        <bytes>0</bytes>
        <bytes>3</bytes>
      </MacAddress>
    </layer2Configuration>
    <ipv4Configuration isActive="true" addressConfiguration="DHCPv4" dhcpOptions="//@Dhcp.0">
      <IpAddress>
        <bytes>0</bytes>
        <bytes>0</bytes>
        <bytes>0</bytes>
        <bytes>0</bytes>
      </IpAddress>
      <Netmask>
        <bytes>-1</bytes>
        <bytes>-1</bytes>
        <bytes>-1</bytes>
        <bytes>0</bytes>
      </Netmask>
      <DefaultGateway>
        <bytes>0</bytes>
        <bytes>0</bytes>
        <bytes>0</bytes>
        <bytes>0</bytes>
      </DefaultGateway>
    </ipv4Configuration>
    <ipv6Configuration isActive="false" addressConfiguration="Fixed" prefixLength="64">
      <IpAddress>
        <bytes>0</bytes>
        <bytes>0</bytes>
        <bytes>0</bytes>
        <bytes>0</bytes>
        <bytes>0</bytes>
        <bytes>0</bytes>
        <bytes>0</bytes>
        <bytes>0</bytes>
        <bytes>0</bytes>
        <bytes>0</bytes>
        <bytes>0</bytes>
        <bytes>0</bytes>
        <bytes>0</bytes>
        <bytes>0</bytes>
        <bytes>0</bytes>
        <bytes>0</bytes>
      </IpAddress>
      <DefaultRouter>
        <bytes>0</bytes>
        <bytes>0</bytes>
        <bytes>0</bytes>
        <bytes>0</bytes>
        <bytes>0</bytes>
        <bytes>0</bytes>
        <bytes>0</bytes>
        <bytes>0</bytes>
        <bytes>0</bytes>
        <bytes>0</bytes>
        <bytes>0</bytes>
        <bytes>0</bytes>
        <bytes>0</bytes>
        <bytes>0</bytes>
        <bytes>0</bytes>
        <bytes>0</bytes>
      </DefaultRouter>
    </ipv6Configuration>
    <ByteBlowerGuiPortConfiguration physicalServerAddress="byteblower-tutorial-1300.lab.byteblower.excentis.com" physicalInterfaceId="0" physicalPortId="44" physicalServerType="ByteBlower"/>
  </ByteBlowerGuiPort>
  <ByteBlowerGuiPort name="Behind NAT_3_No NAT flag" theDestinationOfFlow="//@Flow.2" natted="false" mtu="1500">
    <layer2Configuration xsi:type="byteblowerguimodel_v1_3:EthernetConfiguration">
      <MacAddress>
        <bytes>0</bytes>
        <bytes>-1</bytes>
        <bytes>-69</bytes>
        <bytes>-51</bytes>
        <bytes>0</bytes>
        <bytes>4</bytes>
      </MacAddress>
    </layer2Configuration>
    <ipv4Configuration isActive="true" addressConfiguration="DHCPv4" dhcpOptions="//@Dhcp.0">
      <IpAddress>
        <bytes>0</bytes>
        <bytes>0</bytes>
        <bytes>0</bytes>
        <bytes>0</bytes>
      </IpAddress>
      <Netmask>
        <bytes>-1</bytes>
        <bytes>-1</bytes>
        <bytes>-1</bytes>
        <bytes>0</bytes>
      </Netmask>
      <DefaultGateway>
        <bytes>0</bytes>
        <bytes>0</bytes>
        <bytes>0</bytes>
        <bytes>0</bytes>
      </DefaultGateway>
    </ipv4Configuration>
    <ipv6Configuration isActive="false" addressConfiguration="Fixed" prefixLength="64">
      <IpAddress>
        <bytes>0</bytes>
        <bytes>0</bytes>
        <bytes>0</bytes>
        <bytes>0</bytes>
        <bytes>0</bytes>
        <bytes>0</bytes>
        <bytes>0</bytes>
        <bytes>0</bytes>
        <bytes>0</bytes>
        <bytes>0</bytes>
        <bytes>0</bytes>
        <bytes>0</bytes>
        <bytes>0</bytes>
        <bytes>0</bytes>
        <bytes>0</bytes>
        <bytes>0</bytes>
      </IpAddress>
      <DefaultRouter>
        <bytes>0</bytes>
        <bytes>0</bytes>
        <bytes>0</bytes>
        <bytes>0</bytes>
        <bytes>0</bytes>
        <bytes>0</bytes>
        <bytes>0</bytes>
        <bytes>0</bytes>
        <bytes>0</bytes>
        <bytes>0</bytes>
        <bytes>0</bytes>
        <bytes>0</bytes>
        <bytes>0</bytes>
        <bytes>0</bytes>
        <bytes>0</bytes>
        <bytes>0</bytes>
      </DefaultRouter>
    </ipv6Configuration>
    <ByteBlowerGuiPortConfiguration physicalServerAddress="byteblower-tutorial-1300.lab.byteblower.excentis.com" physicalInterfaceId="0" physicalPortId="44" physicalServerType="ByteBlower"/>
  </ByteBlowerGuiPort>
  <Dhcp name="DHCP_1" MaximumDiscoverRetries="5" InitialDiscoverTimeout="1000000000" MaximumRequestRetries="5" InitialRequestTimeout="1000000000" RetransmissionPolicy="FixedTiming" ipv4Configurations="//@ByteBlowerGuiPort.0/@ipv4Configuration //@ByteBlowerGuiPort.1/@ipv4Configuration //@ByteBlowerGuiPort.2/@ipv4Configuration //@ByteBlowerGuiPort.3/@ipv4Configuration"/>
</byteblowerguimodel_v1_3:ByteBlowerProject>
