<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>InterfaceTopTagsOptionsPage</class>
 <widget class="QWidget" name="InterfaceTopTagsOptionsPage">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>893</width>
    <height>698</height>
   </rect>
  </property>
  <layout class="QVBoxLayout">
   <property name="spacing">
    <number>6</number>
   </property>
   <property name="leftMargin">
    <number>9</number>
   </property>
   <property name="topMargin">
    <number>9</number>
   </property>
   <property name="rightMargin">
    <number>9</number>
   </property>
   <property name="bottomMargin">
    <number>9</number>
   </property>
   <item>
    <widget class="QLabel" name="label">
     <property name="text">
      <string>Show the below tags above all other tags in the metadata view</string>
     </property>
    </widget>
   </item>
   <item>
    <layout class="QHBoxLayout" name="horizontalLayout">
     <item>
      <layout class="QVBoxLayout" name="verticalLayout_2">
       <item>
        <widget class="EditableTagListView" name="top_tags_list">
         <property name="dragEnabled">
          <bool>true</bool>
         </property>
         <property name="dragDropMode">
          <enum>QAbstractItemView::InternalMove</enum>
         </property>
        </widget>
       </item>
       <item>
        <layout class="QHBoxLayout" name="horizontalLayout_2">
         <item>
          <spacer name="horizontalSpacer">
           <property name="orientation">
            <enum>Qt::Horizontal</enum>
           </property>
           <property name="sizeHint" stdset="0">
            <size>
             <width>40</width>
             <height>20</height>
            </size>
           </property>
          </spacer>
         </item>
         <item>
          <widget class="QPushButton" name="tags_remove_btn">
           <property name="toolTip">
            <string>Remove selected tags</string>
           </property>
           <property name="accessibleName">
            <string>Remove selected tags</string>
           </property>
           <property name="text">
            <string>Remove tags</string>
           </property>
          </widget>
         </item>
         <item>
          <widget class="QPushButton" name="tags_add_btn">
           <property name="accessibleName">
            <string/>
           </property>
           <property name="text">
            <string>Add new tag</string>
           </property>
          </widget>
         </item>
        </layout>
       </item>
      </layout>
     </item>
     <item>
      <layout class="QVBoxLayout" name="verticalLayout">
       <item>
        <spacer name="verticalSpacer">
         <property name="orientation">
          <enum>Qt::Vertical</enum>
         </property>
         <property name="sizeHint" stdset="0">
          <size>
           <width>20</width>
           <height>40</height>
          </size>
         </property>
        </spacer>
       </item>
       <item>
        <widget class="QPushButton" name="tags_move_up_btn">
         <property name="toolTip">
          <string>Move tag up</string>
         </property>
         <property name="accessibleName">
          <string>Move tag up</string>
         </property>
         <property name="text">
          <string/>
         </property>
         <property name="icon">
          <iconset theme="go-up">
           <normaloff>.</normaloff>.</iconset>
         </property>
        </widget>
       </item>
       <item>
        <widget class="QPushButton" name="tags_move_down_btn">
         <property name="toolTip">
          <string>Move tag down</string>
         </property>
         <property name="accessibleName">
          <string>Move tag down</string>
         </property>
         <property name="text">
          <string/>
         </property>
         <property name="icon">
          <iconset theme="go-down">
           <normaloff>.</normaloff>.</iconset>
         </property>
        </widget>
       </item>
       <item>
        <spacer name="verticalSpacer_2">
         <property name="orientation">
          <enum>Qt::Vertical</enum>
         </property>
         <property name="sizeHint" stdset="0">
          <size>
           <width>20</width>
           <height>40</height>
          </size>
         </property>
        </spacer>
       </item>
      </layout>
     </item>
    </layout>
   </item>
  </layout>
 </widget>
 <customwidgets>
  <customwidget>
   <class>EditableTagListView</class>
   <extends>QListView</extends>
   <header>picard.ui.taglistview</header>
   <slots>
    <slot>add_empty_row()</slot>
    <slot>remove_selected_rows()</slot>
    <slot>move_selected_rows_up()</slot>
    <slot>move_selected_rows_down()</slot>
   </slots>
  </customwidget>
 </customwidgets>
 <resources/>
 <connections>
  <connection>
   <sender>tags_add_btn</sender>
   <signal>clicked()</signal>
   <receiver>top_tags_list</receiver>
   <slot>add_empty_row()</slot>
   <hints>
    <hint type="sourcelabel">
     <x>804</x>
     <y>673</y>
    </hint>
    <hint type="destinationlabel">
     <x>428</x>
     <y>343</y>
    </hint>
   </hints>
  </connection>
  <connection>
   <sender>tags_remove_btn</sender>
   <signal>clicked()</signal>
   <receiver>top_tags_list</receiver>
   <slot>remove_selected_rows()</slot>
   <hints>
    <hint type="sourcelabel">
     <x>716</x>
     <y>673</y>
    </hint>
    <hint type="destinationlabel">
     <x>428</x>
     <y>343</y>
    </hint>
   </hints>
  </connection>
  <connection>
   <sender>tags_move_up_btn</sender>
   <signal>clicked()</signal>
   <receiver>top_tags_list</receiver>
   <slot>move_selected_rows_up()</slot>
   <hints>
    <hint type="sourcelabel">
     <x>867</x>
     <y>344</y>
    </hint>
    <hint type="destinationlabel">
     <x>428</x>
     <y>343</y>
    </hint>
   </hints>
  </connection>
  <connection>
   <sender>tags_move_down_btn</sender>
   <signal>clicked()</signal>
   <receiver>top_tags_list</receiver>
   <slot>move_selected_rows_down()</slot>
   <hints>
    <hint type="sourcelabel">
     <x>867</x>
     <y>374</y>
    </hint>
    <hint type="destinationlabel">
     <x>428</x>
     <y>343</y>
    </hint>
   </hints>
  </connection>
 </connections>
</ui>